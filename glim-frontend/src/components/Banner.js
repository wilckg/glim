import React from 'react';
import { Container, Row, Col } from 'react-bootstrap';
import bannerBackground from '../assets/background-memori-banner.jpg';
import logo from '../assets/memori-logo-preto.png';


function Banner(){
  return (
    <Container fluid className="p-5 bg-light text-center banner-home"
                style={{backgroundImage: `url(${bannerBackground})`, backgroundSize: 'cover', backgroundPosition: 'center', height: '400px'}}>
      <Row>
        <Col className="banner-coluna">
          <img src={logo} alt="" className="logo-banner" />
          <p>Buscador de memórias, hábitos e heranças.</p>
        </Col>
      </Row>
    </Container>
  )
}

export default Banner;