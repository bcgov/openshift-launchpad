import axios from "axios";

const instance = axios.create({
  baseURL: process.env.API_URL,
});

instance.interceptors.response.use(
  // Automatically unpack the successful response
  response => response.data,
  // Automatically log a failed response and then pass it along
  error => {
    console.error(error);
    return Promise.reject(error);
  }
);

export default instance;
