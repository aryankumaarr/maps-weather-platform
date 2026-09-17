
import Map from "@/components/Map/Map";
import LocationSearch from "@/components/LocationSearch/LocationSearch";

export default function Home() {
  return <main className="main-window">
 <h1>Weather Route</h1>
 <div>Find a safer route based on weather conditions</div>
 <LocationSearch />
 <Map />
  </main>;
   
}
