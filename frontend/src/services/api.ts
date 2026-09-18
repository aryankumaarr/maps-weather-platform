import type { RouteRequest,RouteResponse } from "@/types/routes";
import { request } from "http";

const API_URL = "http://localhost:8000";

export async function getRoute(
request: RouteRequest
): Promise<RouteResponse>{
    const response = await fetch(`${API_URL}/api/route`,{
        method:"POST", headers:{"Content-Type":"application.json"}, body:JSON.stringify(request)
    });

    if(!response.ok){
        throw new Error("Unable to get route");
    }
return response.json();
}

