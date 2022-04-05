import React, { Component } from "react";
import axios from 'axios';

import PlaceInfor, {MyImg} from './place.js'
import PlaceModal from './Modal'


import { Row, Column } from 'react-foundation';

export default class PlaceList extends Component {
    constructor(props) {
        super(props);
        this.state = {
            fdata :  [],
            Img: [],
            type : 0,
            activeItem : {
                id : 0,
                Name : "#",
                Address: "#",
                Description: "#",
                Type: "#",
                Site: "#",
                Tel: "#",
                Type: 0,
            },
        };
        var type = 0;
        if (props.type == "Restauran")
            type = 1;
        else if (props.type == "Museum")
            type = 2;
        else if (props.type == "Sight")
            type = 3;

        console.log(props.type);
        console.log(type);

        if (type != 0)
            this.setState({type : type});
    };

    fetching() {
        console.log("Get Data");
        axios.get('http://127.0.0.1:8000/api/v1/Place/')
        .then(res => {
            var data = res.data;
            if (this.state.type != 0)
               data = data.filter((i)=> i.Type == this.state.type);
            this.setState({ fdata: data });
        console.log(this.state.fdata);
      })
    }

    fetchImg(){
        axios.get('http://127.0.0.1:8000/api/v1/Img/')
        .then(res => {
            var data = res.data;
            this.setState({ Img: data });
      })
    }

    componentDidMount() {
        this.fetching();
        this.fetchImg();
    }

    toggle = () => {
        this.setState({ modal: !this.state.modal });
    };

    createItem = () => {
        alert('Create');
        var item = {
            id : 0,
            Name: "#",
            Address: "#",
            Description: "#",
            Type: "#",
            Site: "#",
            Tel: "#",
            Type: 0,};
        this.setState({activeItem: item, modal: !this.state.modal});

    }

    handleSubmit = (item) => {
        alert("Submit");
        this.toggle();
        var place = {
            id : item.id,
            Name: item.Name,
            Address: item.Address,
            Description: item.Description,
            Type: item.Type,
            Site: item.Site,
            Tel: item.Tel,
            };
        item.Type = 1;
        console.log("Place", place);
        if (place.id) {
            axios({
                method: 'PUT',
                url: 'http://127.0.0.1:8000/api/v1/Place/'+place.id+'/',
                data: place,
                headers:{
                  "Content-Type":"application/json",
                  "accept": "application/json",
                  'Authorization': 'ABC',
                }
            })
        }
        item.id = item.countPlace+100;
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
        if (item.selectedFile)
        {
            var img = {
                name:"abc",
                place : place.id,
                }
            axios({
                method: 'POST',
                url: 'http://127.0.0.1:8000/api/v1/Img/',
                data: img,
                headers:{
                  "Content-Type":"application/json",
                  "accept": "application/json",
                  'Authorization': 'ABC',
                }
            }).then(response => {
                console.log("response");
            });


        }
        alert("SAve OK");
        this.fetching()

    };

    editItem = (item) => {
        alert("Edit Place");
        alert(item.Name);
        console.log("Edit", item);
        this.setState({activeItem: item, modal: !this.state.modal});
    }

    handleDelete = (item) => {
        alert("Deletê Place");
        axios({
            method: 'DELETE',
                url: 'http://127.0.0.1:8000/api/v1/Place/'+item.id+'/',
                headers:{
                  "accept": "application/json",
                  'Authorization': 'ABC',
                }
        })
        .then((res) => this.fetching());
        alert("Delete OK");
    }

    getListImg(){
        const items = this.state.fdata;
        var tmp = [];
        for (var i = 0; i < items.length; i++)
        {
            const place = items[i];
            const url = 'http://127.0.0.1:8000/api/v1/Place/'+place.id+'/';
            const pImg = this.state.Img.filter((i)=> i.place == url);
            tmp.push(pImg);
        }
        return tmp;
    }

    renderItems = () => {
        const items = this.state.fdata;
        var Img = this.getListImg();
        var tmp = [];
        for (var i = 0; i < Img.length; i++)
        {

            if (Img[i] && Img[i][0])
                tmp.push(Img[i][0].img);
            else
                tmp.push("https://image.shutterstock.com/z/stock-vector-search-no-result-found-in-folder-concept-illustration-flat-design-vector-eps-simple-and-modern-1955682460.jpg");
        }
        console.log(tmp);
        return items.map((place, index) => (

            <div className="cartegory-right-content-item">
			    <a href="">
			        <MyImg src={tmp[index]} />
			        <h1>
			            <a href={"/place/" + place.id}>{ place.Name }</a>

			        </h1>
			    </a>

			    <span>
                      <button className="btn btn-secondary mr-2" onClick={() => this.editItem(place)}>
                        Edit
                      </button>
                      <button className="btn btn-danger" onClick={() => this.handleDelete(place)}>
                        Delete
                      </button>
                    </span>
		    </div>
        ));
    }


    render() {
        //this.state.activeItem.Name = "123";
        console.log("List Render ", this.state.activeItem.Name);
        return (
            <>
                <div className="container">
                    <Row>
                        <Row className="cartegory-right-content">
					        <button className="btn btn-primary" onClick={this.createItem}>
                              Add task
                            </button>
					    </Row>

					    <Row className="cartegory-right-content">
					        {this.renderItems()}
					    </Row>
			        </Row>
		        </div>

		        {this.state.modal ? (
                      <PlaceModal activeItem={this.state.activeItem} toggle={this.toggle} onSave={this.handleSubmit}
                        >
                      </PlaceModal>
                    ) : null}
            </>
        )
    }
}