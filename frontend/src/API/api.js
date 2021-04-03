import Axios from 'axios';

export const baseURL = 'http://94.228.113.211/';

export const API = {
    get: ({url, params, ...rest}) =>
        Axios({
            method: 'GET',
            url,
            params,
            baseURL,
            ...rest
        }),
    post: ({url, data, ...rest}) =>
        Axios({
            method: 'POST',
            url,
            data,
            baseURL,
            ...rest
        }),
}