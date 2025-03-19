import React from 'react';
import { Container, Row, Col } from 'react-bootstrap';
import logo from '../assets/memori-logo-horizontal.png'; 
import fatecLogo from '../assets/fatec-logo-sem-fundo.png'; 
import uspLogo from '../assets/usp-logo-sem-fundo.png'; 
import './Footer.css';

function Footer() {
  return (
    <footer className="py-4">
      <Container>
        <Row>
          <Col md={4} className="text-center">
            <img
              src={logo}
              width="200"
              height="100"
              className="d-inline-block align-top mb-2"
              alt="Logo"
            />
          </Col>
          <Col md={4} className="text-center d-flex flex-column justify-content-center align-items-center">
            <img
              src={fatecLogo}
              width="100"
              height="100"
              className="d-inline-block align-top mb-2"
              alt="Fatec Santana de Parnaíba Logo"
            />
            {/* <p>Fatec Santana de Parnaíba</p> */}
            <img
              src={uspLogo}
              width="100"
              height="100"
              className="d-inline-block align-top mb-2"
              alt="USP Logo"
            />
            {/* <p>Universidade de São Paulo</p> */}
          </Col>
          <Col md={4} className="text-justify">
            <h5>Contato</h5>
            <p>Email: contato@memori.com</p>
            <p>Endereço: Rua Exemplo, 123, São Paulo, SP</p>
            <p>Telefone: (11) 1234-5678</p>
          </Col>
        </Row>
      </Container>
    </footer>
  );
}

export default Footer;
