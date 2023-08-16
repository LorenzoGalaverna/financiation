import {createContext, useState} from "react";

const ReportsContext = createContext();

export default ReportsContext;

export const ReportsProvider = ({children}) => {


    const [locations, setLocations] = useState({});
    const [visits, setVisits] = useState({});
    const [ministryDepartments, setMinistryDepartments] = useState({});
    const [faqs, setFaqs] = useState({});
    const [requests, setRequests] = useState();

    let dataHandler = async (item, tokens) => {
        if (Object.keys(item).length === 3) {
            if (item.id_ministry_department !== undefined) {
                toggle(faqs, item)
            } else {
                if (item.id_department !== undefined) {
                    toggle(locations, item)
                    if (Object.keys(locations).length !== 0) {
                        await getVisitFromLocations(tokens).then(r => setVisits(r))
                    } else {
                        setVisits({})
                    }
                } else {
                    toggle(ministryDepartments, item)
                    if (Object.keys(ministryDepartments).length !== 0) {
                        await getFaqFromMinistry(tokens).then(r => setFaqs(r))
                    } else {
                        setFaqs({})
                    }
                }
            }
        } else {
            toggle(visits, item)
        }
    }

    let toggle = (dict, item) => {
        if (item.id in dict) {
            delete dict[item.id]
        } else {
            dict[item.id] = item.id
        }
        console.log(dict)
    }

    let getVisitFromLocations = async (tokens) => {

        let text = Object.keys(locations).join()
        console.log(text)

        let headers = {
            "Content-Type": "application/json",
            "Authorization": "JWT " + String(tokens),
            "Accept": "application/json"
        }
        let response = await fetch(`/api/visits?locs=${text}`, {headers: headers})
        let data = await response.json()
        console.log(data)
        return data
    }

    let getFaqFromMinistry = async (tokens) => {

        let text = Object.keys(ministryDepartments).join()

        let headers = {
            "Content-Type": "application/json",
            "Authorization": "JWT " + String(tokens),
            "Accept": "application/json"
        }
        let response = await fetch(`/api/faqs?deps=${text}`, {headers: headers})
        let data = await response.json()
        return data
    }

    let getRequestsFromVisitDepsFaqs = async (tokens) => {

        let deps = Object.keys(ministryDepartments).join()
        let faqs = Object.keys(ministryDepartments).join()
        let visits = Object.keys(ministryDepartments).join()

        console.log(deps)
        console.log(faqs)
        console.log(visits)


        let headers = {
            "Content-Type": "application/json",
            "Authorization": "JWT " + String(tokens),
            "Accept": "application/json"
        }

        let response = await fetch(`/api/reports?deps=${deps}&faqs=${faqs}&visits=${visits}`, {headers: headers})
        let data = await response.json()
        setRequests(data)
        console.log(requests)

    }


    let contextData = {
        visits: visits,
        locations: locations,
        ministryDepartments: ministryDepartments,
        faqs: faqs,
        dataHandler: dataHandler,
        getRequestsFromVisitDepsFaqs: getRequestsFromVisitDepsFaqs
    }

    return (
        <ReportsContext.Provider value={contextData}>
            {children}
        </ReportsContext.Provider>
    );

}