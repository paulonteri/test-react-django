import axios from "axios";
import { URL } from "../url";

import { GET_DORMS, ADD_DORM, DELETE_DORM } from "./types";

import { createMessage, returnErrors } from "../messages";
import { tokenConfig } from "../auth/auth";

// GET DORMS
export const getDorms = () => (dispatch, getState) => {
    axios
        .get(URL.concat("/api/v2.0/dormitories/"), tokenConfig(getState))
        .then(res => {
            dispatch({
                type: GET_DORMS,
                payload: res.data
            });
        })
        .catch(err =>
            dispatch(returnErrors(err.response.data, err.response.status))
        );
};
