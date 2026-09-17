import "@/components/LocationSearch/LocationSearch.scss";

export default function LocationSearch() {
  return (
    <section className="location-search">
      <h2>Plan Your Route</h2>

      <div className="location-inputs">
        <div className="inputs-container">
          <input
            type="text"
            id="origin"
            placeholder="Enter Starting Location"
          />

          <input
            type="text"
            id="destination"
            placeholder="Enter Destination Location"
          />
        </div>
      </div>
    </section>
  );
}
