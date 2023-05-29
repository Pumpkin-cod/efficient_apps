/* eslint-disable react/no-unescaped-entities */
/* eslint-disable no-unused-vars */
import React from 'react';
import { useForm } from 'react-hook-form';
import { Container, Row, Col, Form, Button } from 'react-bootstrap';
import imageSrc from '../images/Allura - Feedback Session.png';
import '../CSS/LoginPage.css';

function Login() {
    const { register, handleSubmit, formState: { errors } } = useForm();

    const onSubmit = (data) => {
        const { name, email, password, confirmPassword } = data;

        if (!name || !email || !password || !confirmPassword) {
            // Display popup message or error notification
            alert('Please fill in all fields');
            return;
        }

        if (password !== confirmPassword) {
            // Display popup message or error notification
            alert('Passwords do not match');
            return;
        }
        console.log(data);
    };

    return (
        <div className='container-body'>
            <Container className='container-login'>
            <Row className="justify-content-center pt-2 pb-5 ">
                <Col xs={12} md={6} className='ps-2 pe-5'>
                    <h2 className='text-center'>Login</h2>
                    <Form onSubmit={handleSubmit(onSubmit)}>
                        <Form.Group controlId="name">
                            <Form.Label>Name</Form.Label>
                            <Form.Control type="text" {...register('name', { required: true })} />
                            {errors.name && <Form.Text className="error">Name is required</Form.Text>}
                        </Form.Group>
                        <Form.Group controlId="email">
                            <Form.Label>Email</Form.Label>
                            <Form.Control type="email" {...register('email', { required: true, pattern: /^\S+@\S+$/i })} />
                            {errors.email && <Form.Text className="error">Invalid email address</Form.Text>}
                        </Form.Group>
                        <Form.Group controlId="password">
                            <Form.Label>Password</Form.Label>
                            <Form.Control type="password" {...register('password', { required: true, minLength: 6 })} />
                            {errors.password && <Form.Text className="error">Password must be at least 6 characters</Form.Text>}
                        </Form.Group>
                        <Form.Group controlId="confirmPassword">
                            <Form.Label>Confirm Password</Form.Label>
                            <Form.Control type="password" {...register('confirmPassword', { required: true, minLength: 6 })} />
                            {errors.confirmPassword && <Form.Text className="error">Password confirmation is required</Form.Text>}
                        </Form.Group>
                        <Button className='d-block w-100 login-btn' type="submit">Login</Button>
                    </Form>
                    <div className="additional-options">
                        <div className="remember-me">
                            <Form.Check type="checkbox" id="rememberMe" label="Remember Me" {...register('rememberMe')} />
                        </div>
                        <div className="forgot-password">
                            <a href="#">Forgot Password?</a>
                        </div>
                    </div>
                    <div className="signup-message text-center">
                        Don't have an account? <a href="/signup">Sign Up</a>
                    </div>
                </Col>
                <Col xs={12} md={6} style={{backgroundColor: 'green', height: '100%'}} className='login-image'>
                    <img className="img-blush" src={imageSrc} alt="Image" />
                </Col>
            </Row>
        </Container>
        </div>
    );
}

export default Login;

