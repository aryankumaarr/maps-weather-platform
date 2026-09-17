
import Map from "@/components/Map/Map";
import LocationSearch from "@/components/LocationSearch/LocationSearch";
import RouteInfo from '@/components/RouteInfo/RouteInfo'
import WeatherCard from "@/components/WeatherCard/WeatherCard";
export default function Home() {
  return <main className="main-window">
 <LocationSearch />
 <Map />
 <RouteInfo />
 <WeatherCard />
 
  </main>;
   
}
