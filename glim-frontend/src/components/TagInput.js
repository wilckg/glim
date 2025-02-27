import React, { useState } from 'react';
import { InputGroup, FormControl, Button, Badge } from 'react-bootstrap';

import './TagInput.css';

function TagInput() {
  const [tags, setTags] = useState([]);
  const [inputValue, setInputValue] = useState('');

  const handleAddTag = (event) => {
    if ((event.key === 'Enter' || event.type === 'click') && inputValue) {
      if (!tags.includes(inputValue)) {
        setTags([...tags, inputValue]);
      }
      setInputValue('');
    }
  };

  const handleDeleteTag = (tagToDelete) => {
    setTags(tags.filter((tag) => tag !== tagToDelete));
  };

  return (
    <div>
      <InputGroup className="mb-3">
        <FormControl
          placeholder="Add a tag"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          onKeyDown={handleAddTag}
        />
        <Button
          variant="outline-secondary"
          onClick={handleAddTag}
        >
          Add
        </Button>
      </InputGroup>
      <div className="tag-container">
        {tags.map((tag, index) => (
          <Badge
            pill
            bg="primary"
            key={index}
            className="mr-2 badge-custom"
            onClick={() => handleDeleteTag(tag)}
          >
            {tag} <span aria-hidden="true">&times;</span>
          </Badge>
        ))}
      </div>
    </div>
  );
};

export default TagInput;
