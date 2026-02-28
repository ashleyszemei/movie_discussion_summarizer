import React, { useState } from 'react';

const MovieForm = (props) => {

  const handleSubmit = (event) => {
    event.preventDefault();
    var url = props.url;
    if (url) {
      props.generateSummary(url);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div className="form-section">
        <input
          style={{ flexGrow:"1", marginRight:"0.5em" }}
          type="text"
          value={props.url}
          onChange={(e) => resetUrl(e.target.value)}
          placeholder="Select a movie from the list"
          disabled
        />
        <button type="submit">Generate Summary</button>
      </div>
    </form>
  );
};

export default MovieForm;