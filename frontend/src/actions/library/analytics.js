import axios from "axios";
import { URL } from "../url";
import { GET_BOOKS_NUM } from "./types";
import { returnErrors } from "../messages";
import { tokenConfig } from "../auth/auth";

// GET BOOKS
export const getBooksNum = () => (dispatch, getState) => {
    axios
        .get(URL.concat("/api/v2.0/library/booksnum/"), tokenConfig(getState))
        .then(res => {
            dispatch({
                type: GET_BOOKS_NUM,
                payload: res.data
            });
        })
        .catch(err =>
            dispatch(returnErrors(err.response.data, err.response.status))
        );
};
