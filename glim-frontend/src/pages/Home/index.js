import React from 'react'; 
import { Container, Row, Col, Card } from 'react-bootstrap';
import Banner from '../../components/Banner';
import './Home.css';

import cardImage1 from '../../assets/doctor-who-1.webp';
import cardImage2 from '../../assets/doctor-who-2.jpg';
import cardImage3 from '../../assets/doctor-who-3.jpg';
import cardImage4 from '../../assets/doctor-who-4.jpg';

function Home() {
  const cardData = [
    {
      title: 'Card 1',
      text: 'Conteúdo do Card 1',
      imgSrc: cardImage1
    },
    {
      title: 'Card 2',
      text: 'Conteúdo do Card 2',
      imgSrc: cardImage2
    },
    {
      title: 'Card 3',
      text: 'Conteúdo do Card 3',
      imgSrc: cardImage3
    },
    {
      title: 'Card 4',
      text: 'Conteúdo do Card 4',
      imgSrc: cardImage4
    }
  ];

  return (
    <div>
      <Banner />
      <Container fluid className="p-5 bg-light text-center">
        <Row>
          <Col className="home-container">
            <h4>Seja bem vindo ao Memori - Buscador de Memória</h4>
            <div className="home-container-text">
              <p>Nesta página buscamos otimizar as buscas por tipos de memória segundo Bergson</p>
              <p>A memória-hábito é o tipo de conhecimento que é adquirido a partir de repetições cotidianas ou temporais. Ela é bastante usada por estudantes que querem passar numa prova e precisam revisar ou fazer bastante questões.</p>
              <p>Já a memória-pura, depende de um envolvimento emocional. É adquirida muitas vezes até sem querer e pode ser decorrente até de algum trauma.</p>
            </div>
          </Col>
        </Row>
      </Container>
      <Container className="my-5">
        <Row>
          {cardData.map((card, index) => (
            <Col key={index} xs={12} sm={6} md={6} lg={6} className="mb-4 d-flex">
              <Card className="w-100">
                <Row noGutters className="h-100">
                  <Col md={4} className="card-img-container">
                    <Card.Img variant="top" src={card.imgSrc} className="card-img"/>
                  </Col>
                  <Col md={8}>
                    <Card.Body className="d-flex flex-column justify-content-center">
                      <Card.Title>{card.title}</Card.Title>
                      <Card.Text>{card.text}</Card.Text>
                    </Card.Body>
                  </Col>
                </Row>
              </Card>
            </Col>
          ))}
        </Row>
      </Container>
    </div>
  );
}

export default Home;
