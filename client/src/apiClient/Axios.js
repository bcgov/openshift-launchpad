import axios from 'axios';

const Axios = axios.create({
  baseURL: process.env.API_URL,
});

Axios.interceptors.response.use(
  // Automatically unpack the successful response
  (response) => response.data,
  // Automatically log a failed response and then pass it along
  (error) => {
    console.error(error); // eslint-disable-line no-console
    return Promise.reject(error);
  },
);

export default Axios;
