/* eslint-disable no-unused-vars */
import React from 'react';
import { useForm } from 'react-hook-form';
import imageSrc from '../images/Allura - Feedback Session.png';

function SignUp() {
  const { register, handleSubmit, formState: { errors } } = useForm();

  const onSubmit = (data) => {
    console.log(data);
  };

  return (
    <div className='big-container'>
      <div className='container'>
        <h2>Sign Up</h2>
        <form className='login-form' onSubmit={handleSubmit(onSubmit)}>
          <div>
            <label htmlFor='name'>Name</label>
            <input type='text' id='name' {...register('name', { required: true })} />
            {errors.name && <span className='error'>Name is required</span>}
          </div>
          <div>
            <label htmlFor='email'>Email</label>
            <input type='email' id='email' {...register('email', { required: true, pattern: /^\S+@\S+$/i })} />
            {errors.email && <span className='error'>Invalid email address</span>}
          </div>
          <div>
            <label htmlFor='password'>Password</label>
            <input type='password' id='password' {...register('password', { required: true, minLength: 6 })} />
            {errors.password && <span className='error'>Password must be at least 6 characters</span>}
          </div>
          <div>
            <label htmlFor='confirmPassword'>Confirm Password</label>
            <input type='password' id='confirmPassword' {...register('confirmPassword', { required: true, minLength: 6 })} />
            {errors.confirmPassword && <span className='error'>Password confirmation is required</span>}
          </div>
          <button type='submit'>Sign Up</button>
        </form>
        <div className='additional-options'>
          <div className='remember-me'>
            <input type='checkbox' id='rememberMe' {...register('rememberMe')} />
            <label htmlFor='rememberMe'>Remember Me</label>
          </div>
          <div className='forgot-password'>
            <a href='#'>Forgot Password?</a>
          </div>
        </div>
        <div className='signup-message'>
          Already have an account? <a href='/login'>Login</a>
        </div>
      </div>
      <div className='img-container'>
        <img className='img-blush' src={imageSrc} alt='Image' />
      </div>
    </div>
  );
}

export default SignUp;
