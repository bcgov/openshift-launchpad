import React from 'react';
import { shallow } from 'enzyme';

import Home from '@/components/Home';

describe('Home - unit', () => {
  
  it('renders correctly', () => {
    const wrapper = shallow(<Home />);
    expect(wrapper).toMatchSnapshot();
  });
  
});
