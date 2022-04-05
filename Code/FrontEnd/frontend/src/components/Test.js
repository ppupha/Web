import React, { Component } from "react";
import axios from 'axios';





export default class Test extends Component {
    constructor(props) {
        super(props);
        this.state = {
            data :  [],
        };
    };

    fetching() {
        axios({
                method: 'GET',
                url: 'http://127.0.0.1:8000/api/v1/City/1/',
                headers:{
                  "accept": "application/json",
                  'Authorization': 'ABC',
                }
        })
             .then(res => {
                    this.setState({data: res.data});
                    });
    }
    componentDidMount() {
        this.fetching();
    }
    submitForm(event) {
       //Chặn sự kiện mặc định của form
       event.preventDefault()
       alert("Submit");
       //In ra giá trị của input trong form
       const item = {
            id : 1003,
            Name: "gdggf ",
            Address: "#",
            Description:  "#",
            Type: "#",
            Site: "#",
            Tel: "#",
            Type: 0,};

            axios({
                method: 'POST',
                url: 'http://127.0.0.1:8000/api/v1/Place/',
                data: item,
                headers:{
                  "Content-Type":"application/json",
                  "accept": "application/json",
                  'Authorization': 'ABC',
                }
            }).then(response => {
                console.log("response");
            });

        }

    submitForm1(event){
        console.log("Submit");
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json', 'X-CSRFToken': 'K77EOMyscCL2T7YkSGU5yhhAbBtDIf9biTG6x5BKh4Ihlplkejhyd1wdsKP0hTaH' },
            body: JSON.stringify({id: 100, Name: 'ABC',}),
        };
        fetch('http://127.0.0.1:8000/api/v1/City/', requestOptions)
        .then(response => response.json())
        .then(data => alert(JSON.stringify(data)));
    }


    render() {

        return (
            <>
                <div>{this.state.data.id}</div>
                <form className="form-horizontal" onSubmit={(event) => {this.submitForm(event)}}>
                    <div className="form-group">
                        <div className="col-md-10 col-sm-9 col-xs-12 col-md-push-2 col-sm-push-3 col-xs-push-0">
                            <input className="btn btn-primary" type="submit" value="Update Profile"/>
                        </div>
                    </div>
                </form>

            </>
        );
    }
}




