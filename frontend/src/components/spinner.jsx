import React from 'react';

export default function Spinner({text}) {
  return (
    <div>
      <img src="./spinner.svg" width={50}/>
      <p>{text}</p>
    </div>
  );
}