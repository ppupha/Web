import React, { Component } from "react";
import axios from 'axios';


import MyNavbar from './navbar.js'
import Place, {MyPanel} from './place.js'
import Footer from './footer.js'


class Review extends Component {
    constructor(props) {
        super(props);
        this.state = {
            fdata :  [],
            activeItem : {
                Name : "",
            },
        };
    };

    render() {

        return (
            <>
                <li class="media">
                    <a href="#" class="pull-left">
                        <img src={require("../static/img/img1.jpg")} class="img-circle comment-avatar"/>
                    </a>
                    <div class="media-body">
                            <div className="rate pull-right show-rating rating5">
                            <span class="fa fa-star"></span>
                            <span class="fa fa-star"></span>
                            <span class="fa fa-star"></span>
                            <span class="fa fa-star"></span>
                            <span class="fa fa-star"></span>
                            </div>
                        <strong class="text-success">@ {this.props.username} </strong>
                        <p>
                            {this.props.comment}
                        </p>
                    </div>
                </li>
            </>
        )
    }
}


export default class ReviewList extends Component {
    constructor(props) {
        super(props);
        this.state = {
            fdata :  [],
            username: [],
            placeURL: "",
        };
    };

    fetching() {
        this.state.placeURL = 'http://127.0.0.1:8000/api/v1/Place/'+ this.props.placeid+'/';
        axios.get('http://127.0.0.1:8000/api/v1/Review/')
        .then(res => {
            const fdata = res.data.filter((i)=> i.place == this.state.placeURL);
            this.setState({ fdata: fdata });
      })
    }

    componentDidMount() {
        this.fetching();
    }

    renderItems(){
        const items = this.state.fdata;
        var tmp = [];
        for (var i = 0; i < items.length; i++)
        {
            var ele = items[i];
            axios.get(ele.auth)
                    .then((res)=>{
                        this.state.username = res.data.username;
                        console.log(this.state.username);
                        console.log(res.data)});

                console.log(this.state.username);
                tmp.push(
                    <Review rating={ele.rating} comment={ele.comment} username={this.state.username}></Review>
                );
        }
        return tmp;
    }



    render() {

        return (
            <>
                <MyPanel heading="Comment">
                    <form></form>

                    <div class="clearfix"></div>

                    <ul class="media-list">
                        <Review rating="5" username="UserNAme" comment="This is COmment"></Review>
                        {this.renderItems()}
                    </ul>
                </MyPanel>

            </>
        );
    }
}




