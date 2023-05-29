/* eslint-disable no-irregular-whitespace */
/* eslint-disable no-unused-vars */
import React from 'react';
import { Container, Row, Col, Button } from 'react-bootstrap';
import imageSrc from '../images/Hero.png';
import "../CSS/Hero.css"

function HeroSection() {
    return (
        <Container fluid className="hero-section p-5">
            <Row className="m-0">
                <Col md={6} className="left-div p-0">
                    <div className="hero-content">
                        <h1 style={{ color: 'blue' }}>Efficient Corporates.</h1>
                        <h1>Anything Can Be Automated.</h1>
                        <h3>Stop Managing your Businesses the Old Way. Adopt Technology, Digitize your Workspace and Automate your Tasks.</h3>
                    </div>
                    <Button variant="primary" className="hero-button button">Get Started</Button>
                </Col>
                <Col md={6} className="right-div p-0">
                    <img src={imageSrc} alt="Hero Image" className="hero-image" />
                </Col>
            </Row>
        </Container>
    );
}

export default HeroSection;

