
import * as React from "react";
import {
  Input,
} from "reactstrap";

const MyInput = (props) => {

    const [inputValue, setInputValue] = React.useState(props.value);

        const onChangeHandler = event => {
            setInputValue(event.target.value);
        };

        return (
            <Input
              type={props.type}
              name={props.name}
              className={props.className}
              value={inputValue}
              placeholder={props.placeholder}
              onChange={onChangeHandler}
            />
        );

};
export default MyInput;