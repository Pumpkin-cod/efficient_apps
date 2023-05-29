/* eslint-disable no-unused-vars */
import React from 'react';
import { Container, Row, Col, Button } from 'react-bootstrap';
import imageSrc from '../images/Hero.png';
import "../CSS/Hero.css"

function HeroSection() {
    return (
        <Container fluid className="hero-section p-5">
            <Row>
                <Col md={6} className="left-div ps-5">
                    <div className="hero-content">
                        <p>Say goodbye to manual data entry and complicated spreadsheets. 
                        Our powerful GSTR reconciliation software makes the process accurate and hassle-free..</p>
                    </div>
                    <Button variant="primary" className="hero-button button">Get Started</Button>
                </Col>
                <Col md={6} className="right-div">
                    <img src={imageSrc} alt="Hero Image" className="hero-image" />
                </Col>
            </Row>
        </Container>
    );
}

export default HeroSection;
