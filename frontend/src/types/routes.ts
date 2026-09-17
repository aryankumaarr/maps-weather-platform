

export type Location = {
  name: string;
  latitiude: number;
  longitude: number;
};

export type RouteRequest = {
  origin: Location;
  destination: Location;
};

export type RouteSegment = {
  start: Location;
  end: Location;
  weatherRisk: string;
  weatherReasons: string[];
};

export type Route = {
  distanceKm: number;
  durationMinutes: number;
  polyline?: string;
  segments: RouteSegment[];
};

export type WeatherAnalysis = {
  overallRisk: string;
  conditions: string[];
};

export type RouteResponse = {
  route: Route;
  weatherAnalysis: WeatherAnalysis;
  alternativeRoute?: Route | null;
  recommendation: string;
  reason?: string;
};
