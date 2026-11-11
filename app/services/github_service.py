
import httpx

GITHUB_API_URL = "https://api.github.com"

HEADERS = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"
}


# Get repository information
async def get_repository(owner: str, repo: str):

    url = f"{GITHUB_API_URL}/repos/{owner}/{repo}"

    async with httpx.AsyncClient(timeout=15.0) as client:

        response = await client.get(url, headers=HEADERS)

        response.raise_for_status()

        return response.json()


# Get all open pull requests
async def get_pull_requests(owner: str, repo: str):

    url = f"{GITHUB_API_URL}/repos/{owner}/{repo}/pulls"

    async with httpx.AsyncClient(timeout=15.0) as client:

        response = await client.get(
            url,
            params={"state": "open"},
            headers=HEADERS
        )

        response.raise_for_status()

        return response.json()


# Get one pull request
async def get_pull_request(
    owner: str,
    repo: str,
    pr_number: int
):

    url = (
        f"{GITHUB_API_URL}/repos/"
        f"{owner}/{repo}/pulls/{pr_number}"
    )

    async with httpx.AsyncClient(timeout=15.0) as client:

        response = await client.get(url, headers=HEADERS)

        response.raise_for_status()

        return response.json()


# Get files changed in a pull request
async def get_pull_request_files(
    owner: str,
    repo: str,
    pr_number: int
):

    url = (
        f"{GITHUB_API_URL}/repos/"
        f"{owner}/{repo}/pulls/{pr_number}/files"
    )

    async with httpx.AsyncClient(timeout=15.0) as client:

        response = await client.get(url, headers=HEADERS)

        response.raise_for_status()

        return response.json()
