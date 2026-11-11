
import httpx

from fastapi import APIRouter, HTTPException
from app.services.diff_service import process_pull_request_files

from app.services.github_service import (
    get_repository,
    get_pull_requests,
    get_pull_request,
    get_pull_request_files
)


router = APIRouter(
    prefix="/github",
    tags=["GitHub"]
)


# Handle GitHub API errors
def handle_github_error(error: httpx.HTTPStatusError):

    status_code = error.response.status_code

    if status_code == 404:
        raise HTTPException(
            status_code=404,
            detail="GitHub repository or pull request not found"
        )

    if status_code == 403:
        raise HTTPException(
            status_code=502,
            detail="GitHub API access is restricted"
        )

    raise HTTPException(
        status_code=502,
        detail="GitHub API request failed"
    )


# Get repository information
@router.get("/repositories/{owner}/{repo}")
async def fetch_repository(owner: str, repo: str):

    try:

        repository = await get_repository(owner, repo)

        return {
            "name": repository["name"],
            "full_name": repository["full_name"],
            "description": repository["description"],
            "private": repository["private"],
            "html_url": repository["html_url"],
            "default_branch": repository["default_branch"]
        }

    except httpx.HTTPStatusError as error:
        handle_github_error(error)

    except httpx.RequestError:
        raise HTTPException(
            status_code=502,
            detail="Unable to connect to GitHub"
        )


# Get all open pull requests
@router.get("/repositories/{owner}/{repo}/pulls")
async def fetch_pull_requests(owner: str, repo: str):

    try:

        pull_requests = await get_pull_requests(owner, repo)

        return [
            {
                "number": pr["number"],
                "title": pr["title"],
                "state": pr["state"],
                "html_url": pr["html_url"],
                "user": pr["user"]["login"],
                "created_at": pr["created_at"]
            }
            for pr in pull_requests
        ]

    except httpx.HTTPStatusError as error:
        handle_github_error(error)

    except httpx.RequestError:
        raise HTTPException(
            status_code=502,
            detail="Unable to connect to GitHub"
        )


# Get individual pull request
@router.get(
    "/repositories/{owner}/{repo}/pulls/{pr_number}"
)
async def fetch_pull_request(
    owner: str,
    repo: str,
    pr_number: int
):

    try:

        pr = await get_pull_request(owner, repo, pr_number)

        return {
            "number": pr["number"],
            "title": pr["title"],
            "body": pr["body"],
            "state": pr["state"],
            "html_url": pr["html_url"],
            "user": pr["user"]["login"],
            "head_branch": pr["head"]["ref"],
            "base_branch": pr["base"]["ref"],
            "created_at": pr["created_at"],
            "updated_at": pr["updated_at"],
            "merged": pr["merged"]
        }

    except httpx.HTTPStatusError as error:
        handle_github_error(error)

    except httpx.RequestError:
        raise HTTPException(
            status_code=502,
            detail="Unable to connect to GitHub"
        )


# Get changed files and code diffs
@router.get(
    "/repositories/{owner}/{repo}/pulls/{pr_number}/files"
)
async def fetch_pull_request_files(
    owner: str,
    repo: str,
    pr_number: int
):

    try:

        files = await get_pull_request_files(
            owner,
            repo,
            pr_number
        )

        return [
            {
                "filename": file["filename"],
                "status": file["status"],
                "additions": file["additions"],
                "deletions": file["deletions"],
                "changes": file["changes"],
                "patch": file.get("patch")
            }
            for file in files
        ]

    except httpx.HTTPStatusError as error:
        handle_github_error(error)

    except httpx.RequestError:
        raise HTTPException(
            status_code=502,
            detail="Unable to connect to GitHub"
        )


# Get processed pull request diffs
@router.get(
    "/repositories/{owner}/{repo}/pulls/{pr_number}/diff"
)
async def fetch_processed_diff(
    owner: str,
    repo: str,
    pr_number: int
):

    try:

        files = await get_pull_request_files(
            owner,
            repo,
            pr_number
        )

        processed_files = process_pull_request_files(files)

        return {
            "repository": f"{owner}/{repo}",
            "pull_request": pr_number,
            "total_files": len(files),
            "analyzable_files": len(processed_files),
            "files": processed_files
        }

    except httpx.HTTPStatusError as error:
        handle_github_error(error)

    except httpx.RequestError:
        raise HTTPException(
            status_code=502,
            detail="Unable to connect to GitHub"
        )
