export const getUserStatusesById = async (tokens, statusId) => {

    let headers = {
        "Content-Type": "application/json",
        "Authorization": "JWT " + String(tokens),
        "Accept": "application/json"
    }

    let response = await fetch(`/api/statuses/${statusId}`, {headers: headers})
    let data = await response.json()
    return data
}