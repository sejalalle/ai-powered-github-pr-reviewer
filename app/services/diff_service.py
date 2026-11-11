
def process_pull_request_files(files):

    processed_files = []

    for file in files:

        patch = file.get("patch")

        if patch is None:
            continue

        processed_files.append({
            "filename": file["filename"],
            "status": file["status"],
            "additions": file["additions"],
            "deletions": file["deletions"],
            "changes": file["changes"],
            "patch": patch
        })

    return processed_files
