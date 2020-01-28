import Enzyme from "enzyme";
import Adapter from "enzyme-adapter-react-16";

Enzyme.configure({ adapter: new Adapter() });

// Global settings that have historically been useful/necessary
global.requestAnimationFrame = callback => {
  setTimeout(callback, 0);
};

const location = JSON.stringify(window.location);
delete window.location;

Object.defineProperty(window, "location", {
  value: JSON.parse(location),
});

Object.defineProperty(global.location, "href", {
  value: "http://localhost",
  configurable: true,
});
