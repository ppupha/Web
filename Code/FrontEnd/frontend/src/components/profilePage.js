import React, { Component } from "react";

import MyNavbar from './navbar.js'
import Footer from './footer.js'
import axios from 'axios';

import {MyImg} from './place.js'

import '../static/css/profile.css'




export default class ProfilePage extends Component {
    constructor(props) {
        super(props);
        this.state = {
            data :  [],
            id: "1",
            userid: "",
            username: "",
            email: "",
            firstname: "",
            lastname: "",
        };
    };

    fetching() {
        var id = '9';
        axios.get('http://127.0.0.1:8000/api/v1/Profile/'+id+'/')
             .then(res => {
                    this.setState({ data: res.data }, () => console.log(this.state.data));
                    axios.get(res.data.user)
                            .then(r => {
                                this.setState( {userid: r.data.id,
                                                username: r.data.username,
                                                email: r.data.email,
                                                firstname: r.data.first_name,
                                                lastname: r.data.last_name, }, () => console.log("From Fetch", this.state))
                            })

                    });
    }

    componentDidMount() {
        this.fetching();
    }
    submitForm(event) {
       //Chặn sự kiện mặc định của form
       event.preventDefault()
       //In ra giá trị của input trong form
       const user = {
            username: event.target.username.value,
            email: event.target.email.value,
            first_name: event.target.firstname.value,
            last_name: event.target.lastname.value,
        }
        console.log(user);
        if (this.state.userid) {
            axios({
                method: 'PUT',
                url: 'http://127.0.0.1:8000/api/v1/User/'+this.state.userid + '/',
                data: user,
                headers:{
                  "Content-Type":"application/json",
                  "accept": "application/json",
                  'Authorization': 'ABC',
                }
            }).then(response => {
                console.log("response");
            }).catch((error) => {
                console.log('Error: ', error)
            });
            return;
        }
     }

    changeInputValue(e) {
        this.setState({
          [e.target.name]: e.target.value
        });
    }

    validationForm() {
        let returnData = {
          error : false,
          msg: ''
        }
        const email = this.state.email;
        //Kiểm tra email
        const re = /\S+@\S+\.\S+/;
        if (!re.test(email)) {
          returnData = {
            error: true,
            msg: 'Không đúng định dạng email'
          }
        }
        return returnData;
      }

    profileForm(){

        return (
            <>
                <form class="form-horizontal" onSubmit={(event) => {this.submitForm(event)}}>

                    <fieldset class="fieldset">
                        <div class="form-group">
                            <label htmlFor="text">User Name</label>
                            <input type="text" className="form-control" name="username" value={this.state.username}
                                placeholder="Enter Username" onChange={e => this.changeInputValue(e)}/>
                        </div>

                        <div class="form-group">
                            <label htmlFor="text">First Name</label>
                            <input type="text" className="form-control" name="firstname" value={this.state.firstname}
                                placeholder="Enter First Name" onChange={e => this.changeInputValue(e)}/>
                        </div>
                        <div class="form-group">
                            <label htmlFor="text">Last Name</label>
                            <input type="text" className="form-control" name="lastname" value={this.state.lastname}
                                placeholder="Enter Last Name" onChange={e => this.changeInputValue(e)}/>
                        </div>
                    </fieldset>
                    <fieldset class="fieldset">
                        <div class="form-group">
                            <label htmlFor="text">Email</label>
                            <input type="text" className="form-control" name="email" value={this.state.email}
                                placeholder="Enter Email" onChange={e => this.changeInputValue(e)}/>
                        </div>


                    </fieldset>
                    <div class="form-group">
                        <div class="col-md-10 col-sm-9 col-xs-12 col-md-push-2 col-sm-push-3 col-xs-push-0">
                            <input class="btn btn-primary" type="submit" value="Update Profile"/>
                        </div>
                    </div>
                </form>
            </>
        );

    }

    renderProfile(){
        return (
            <>

            <div class="container">
                <div class="view-account">
                    <section class="module">
                        <div class="module-inner">


                            <div class="content-panel">
                                <h2 class="title">Profile</h2>
                                {this.profileForm()}
                            </div>
                        </div>
                    </section>
                </div>
            </div>
            </>
        );
    }

    render() {
        return (
        <>
            <MyNavbar/>
            {this.renderProfile()}
            <Footer/>
        </>

        )
    }
}