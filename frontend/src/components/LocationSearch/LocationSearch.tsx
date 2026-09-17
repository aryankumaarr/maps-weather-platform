"use client";
import "@/components/LocationSearch/LocationSearch.scss";
import { useState } from "react";

export default function LocationSearch() {
  const [origin,setOrigin] = useState("");
  const [destination,setDestination] = useState("");
   
  return (
    <section className="location-search">
      <h2>Plan Your Route</h2>

      <div className="location-inputs">
        <div className="inputs-container">
          <input
            type="text"
            id="origin"
            value={origin}
            onChange={(event)=>setOrigin(event.target.value)}
            placeholder="Enter Start Location"
          />

          <input
            type="text"
            id="destination"
            value={destination}
            onChange={(event)=>setDestination(event.target.value)}
            placeholder="Enter Destination"
          />
        </div>
      </div>

      <button type="button">Find Route</button>
    </section>
  );
}
