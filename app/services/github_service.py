
import httpx


GITHUB_API_URL = "https://api.github.com"


async def get_repository(owner: str, repo: str):

    url = f"{GITHUB_API_URL}/repos/{owner}/{repo}"

    async with httpx.AsyncClient(timeout=15.0) as client:

        response = await client.get(
            url,
            headers={
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28"
            }
        )

        response.raise_for_status()

        return response.json()
