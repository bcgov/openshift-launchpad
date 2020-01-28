import React from "react";
import { shallow } from "enzyme";
import Home from "@/components/Home";

// Example snapshot test for component regression testing
it("renders correctly with no name", () => {
  const component = shallow(<Home />);
  expect(component).toMatchSnapshot();
});

// Example snapshot test with props provided
it("renders correctly with a name", () => {
  const component = shallow(<Home name="Developer" />);
  expect(component).toMatchSnapshot();
});
