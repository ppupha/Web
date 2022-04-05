import React, { Component } from "react";
import axios from 'axios';


import { Row, Column } from 'react-foundation';



export class MyImg extends Component {
    constructor(props) {
        super(props);
        this.state = {
            data :  [],
            };
        };

    render(){
        return (
        <>
            <img src={this.props.src}/>
        </>
        );
    }
}


export class MyPanel extends Component {
    constructor(props) {
        super(props);
        this.state = {
            data :  [],
        };
    };

    render() {
        return(
            <>
                <div class="panel panel-info" style={{width:'100%', overflow:'auto'}}>
                    <div class="panel-heading">
                        {this.props.heading}
                    </div>
                    <div class="panel-body">
                        {this.props.children}
                    </div>
                </div>
            </>
        )
    }
}

export default class Place extends Component {
    constructor(props) {
        super(props);
        this.state = {
            data :  [],
            Img: [],
            placeURL : "",
            activeItem : {
                Name : "",
            },
        };
    };

    fetching() {
        var id = this.props.placeid;
        axios.get('http://127.0.0.1:8000/api/v1/Place/'+ id+'/')
        .then(res => {
            const data = res.data;
            this.setState({ data: res.data });
      })
    }

    componentDidMount() {
        this.fetching();
    }

    renderPlaceInfor() {
        if (!this.state.data)
            return;
        return (
            <>

                <div class="contain" style={{width:'100%', overflow:'auto'}}>
                    <MyPanel heading="Description">
                        {this.state.data.Description}
                    </MyPanel>
                    <MyPanel heading="Information">
                        <div class = "">Address: {this.state.data.Adress}</div>
                        <div class = "">Telephone: {this.state.data.Tel}</div>
                        <div class = ''>Website: <a href=""> {this.state.data.Site}</a></div>
                    </MyPanel>
                    <MyPanel heading="More">
                        <div > LANG NHA BANG 2</div>
                    </MyPanel>
                </div>
            </>
        );
    }

    render() {
        const place = this.state.data;
        console.log("From Place Render");
        console.log(place);
        this.state.placeURL = 'http://127.0.0.1:8000/api/v1/Place/'+ place.id+'/';
        console.log(this.state.placeURL);

        axios.get('http://127.0.0.1:8000/api/v1/Img/')
             .then(res => {
                    this.state.Img = res.data.filter((i)=> i.place == this.state.placeURL);;
                });


        console.log(this.state.Img);
        const I = this.state.Img;
        var Imgurls = []

            for (var i = 0; i < 5; i++)
                if (I[i])
                    Imgurls.push(I[i].img);
                else Imgurls.push("https://image.shutterstock.com/z/stock-vector-search-no-result-found-in-folder-concept-illustration-flat-design-vector-eps-simple-and-modern-1955682460.jpg");



        return (
            <section className = "product">
                <div className="container">
                    <div className="product-content row">
                        <Row className="product-content-left">
                            <div className="product-content-left-big-img">

                                <MyImg src={Imgurls[0]} />
                            </div>

                            <div className="product-content-left-small-img">
                                <MyImg src={Imgurls[1]} />
                                <MyImg src={Imgurls[2]} />
                                <MyImg src={Imgurls[3]} />
                                <MyImg src={Imgurls[4]} />
                            </div>

                        </Row>

                        <div className="product-content-right">
                            <div className="product-content-right-product-name">
                                <h1>{ place.Name }</h1>
                            </div>

                            <div className="product-content-right-product-rating">
                                <p>Rating 4/5</p>
                            </div>
                        </div>
                    {this.renderPlaceInfor()}
                    </div>


                </div>

            </section>
        )
    }
}