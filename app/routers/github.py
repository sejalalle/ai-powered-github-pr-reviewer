
import httpx

from fastapi import APIRouter, HTTPException

from app.services.github_service import get_repository


router = APIRouter(
    prefix="/github",
    tags=["GitHub"]
)


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

        if error.response.status_code == 404:
            raise HTTPException(
                status_code=404,
                detail="GitHub repository not found"
            )

        if error.response.status_code == 403:
            raise HTTPException(
                status_code=502,
                detail="GitHub API access is currently restricted"
            )

        raise HTTPException(
            status_code=502,
            detail="GitHub API request failed"
        )

    except httpx.RequestError:

        raise HTTPException(
            status_code=502,
            detail="Unable to connect to GitHub"
        )
