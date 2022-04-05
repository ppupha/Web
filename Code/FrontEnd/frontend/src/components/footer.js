import React, { Component } from "react";

export default class Footer extends Component {
    render() {
        return (
        <>
            <div className = "footer-top">

                <li><a href=""> Liên Hệ</a></li>
                <li><a href=""> Giới Thiệu</a></li>
                <li>
                    <a href="" className = "fab fa-facebook-f"></a>
                </li>
            </div>

            <div className = "footer-bottom">
                @NguyenPhuocSang
            </div>
        </>
        )
    }
}