// frontend/src/components/Modal.js

import React, { Component } from "react";
import {
  Button,
  Modal,
  ModalHeader,
  ModalBody,
  ModalFooter,
  Form,
  FormGroup,
  Input,
  Label
} from "reactstrap";
import MyInput from './MyInput.js'
import axios from 'axios';


export default class PlaceModal extends Component {
  constructor(props) {
    super(props);
    console.log("prop PModal   ", props);
    this.state = {
        id : props.activeItem.id,
        Name : props.activeItem.Name,
        Address: props.activeItem.Address,
        Description: props.activeItem.Description,
        Type: props.activeItem.Type,
        Site: props.activeItem.Site,
        Tel: props.activeItem.Tel,
        Type: 0,
        selectedFile : null,
        countPlace : 0,

    };

        axios.get('http://127.0.0.1:8000/api/v1/Place/')
        .then(res => {
            this.setState({ countPlace: res.data.length });
      })
  }
  changeInputValue(e) {
          this.setState({ [e.target.name] : e.target.value});
    }
  onFileChange = event => {
      // Update the state
      this.setState({ selectedFile: event.target.files[0] });
    };

  render() {
    const {  toggle, onSave } = this.props;
    return (
      <Modal isOpen={true} toggle={toggle} style={{opacity:1}} fade={false}>
        <ModalBody>
          <Form>
            <FormGroup>
              <Label for="title">Name</Label>
              <Input type="text" name="Name" value={this.state.Name} placeholder="Enter Place Name"
                onChange={e => this.changeInputValue(e)}/>
            </FormGroup>

            <FormGroup>
              <Label for="title">Address</Label>
              <Input type="text" name="Address" value={this.state.Address} placeholder="Enter Place Address"
                onChange={e => this.changeInputValue(e)}/>
            </FormGroup>

            <FormGroup>
              <Label for="title">Site</Label>
              <Input type="text" name="Site" value={this.state.Site} placeholder="Enter Place Name"
                onChange={e => this.changeInputValue(e)}/>
            </FormGroup>

            <FormGroup>
              <Label for="description">Description</Label>
              <Input type="text" name="Description"  value={this.state.Description}
                placeholder="Enter Place description" onChange={e => this.changeInputValue(e)}/>
             </FormGroup>

             <FormGroup>
              <Label for="title">Tel</Label>
              <Input type="text" name="Tel" value={this.state.Tel} placeholder="Enter Place Tel"
                onChange={e => this.changeInputValue(e)}/>
            </FormGroup>

             <input type="file" name="Image" onChange={this.onFileChange} />

          </Form>
        </ModalBody>
        <ModalFooter>
          <Button color="success" onClick={() => onSave(this.state)}>
            Save
          </Button>
        </ModalFooter>
      </Modal>
    );
  }
}