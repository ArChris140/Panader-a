import React from 'react';
import styled from 'styled-components';

const StyledContainer = styled.div`
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f4f4f4;
`;

const StyledTitle = styled.h1`
  color: #3498db;
  font-size: 24px;
`;

const StyledButton = styled.button`
  background-color: #3498db;
  color: #fff;
  padding: 10px 20px;
  border: none;
  cursor: pointer;
  font-size: 16px;
  border-radius: 4px;
`;

const MyComponent = () => {
  return (
    <StyledContainer>
      <StyledTitle>¡Hola, mundo!</StyledTitle>
      <p>Este es un componente React con estilos usando styled-components.</p>
      <StyledButton>Click me</StyledButton>
    </StyledContainer>
  );
};

export default MyComponent;
