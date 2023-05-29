/* eslint-disable react/no-unescaped-entities */
/* eslint-disable no-unused-vars */
import React from 'react';
import { Container, Row, Col, Image, Card } from 'react-bootstrap';
import imageSrc from '../assets/about us.png'
import '../CSS/About.css'

const About = () => {
    const cardData = [
        { title: 'Satisfied Clients', count: 87 },
        { title: 'Projects Completed', count: 150 },
        { title: 'Accolades Earned', count: 28 },
        { title: 'Awards Earned', count: 50 }
    ];

    return (
        <div className='background'>
        <Container className='pt-2 pb-4 container-about'>
            <h1 className='text-center pb-2' style={{ color: '#F2A229', fontFamily:'Imprima, sans-serif'}}>ABOUT US</h1>
            <Row>
                <Col xs={12} md={6}>
                    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100%', fontFamily: 'Imprima, sans-serif' }}>
                        <Image src={imageSrc} alt="About Image" style={{ width: '100%', height: '100%' }} />
                    </div>
                </Col>
                <Col xs={12} md={6}>
                        <div style={{fontFamily: 'Imprima, sans-serif'}}>
                        Efficient Corporates Pvt Ltd is an Indian Company working towards providing automation solutions to our clients and helping them adopt technology in their daily work.
                        <br />
                        <br />
                        We believe in empowering the root-level employees who are working day in and day out with spreadsheets and doing a major chunk of their work manually. According to a study, working manually on Excel spreadsheets has a 50% more chance of an error. Such errors can lead to wrong data insights, misguided analysis, and in the worst case, direct financial loss to the corporation.
                        <br />
                        <br />
                        We target minimizing such manual tasks in your corporation to the maximum extent possible by providing automated solutions at the best possible costs.
                        <br />
                        <br />
                        Furthermore, we believe that providing an application is not always the best solution since the application requirements differ from client to client. Hence, we also empower and impart relevant knowledge regarding the app so that the client can modify and make changes to the app themselves, with very little or even no coding knowledge.
                        <br />
                        <br />
                        So, next time whenever you find any of your employees doing any tasks manually, remember you've got our back for automation of all such tasks!
                    </div>
                </Col>
            </Row>

                <h1 className='text-center pt-5 pb-2' style={{ color: '#F2A229', fontFamily: 'Imprima, sans-serif' }}> Some Numbers</h1>
                <Row className='pt-5' style={{ fontFamily: 'Imprima, sans-serif' }}>
                    {cardData.map((card, index) => (
                        <Col xs={12} md={3} key={index}>
                            <Card className='glassmorphic-card'>
                                <Card.Body>
                                    <Card.Text style={{ fontSize: '3rem', color: 'green' }}>{card.count}</Card.Text>
                                    <Card.Title style={{ fontSize: '1.5rem'}}>{card.title}</Card.Title> 
                                </Card.Body>
                            </Card>
                        </Col>
                    ))}
                </Row>
        </Container>
        </div>
    );
};

export default About;