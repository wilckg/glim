import React, { useState } from "react";
import { Container, Row, Col, InputGroup, FormControl, Button, Badge, Form } from 'react-bootstrap';
import api from '../../services/api';

import './Buscador.css'

function Buscador() {

    const [tags, setTags] = useState([]);
    const [inputValue, setInputValue] = useState('');
    const [fileType, setFileType] = useState('');
    const [file, setFile] = useState(null);

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

    const changeFileType = (event) => {
        setFileType(event.target.value);
    };

    const handleSubmit = async (event) => {
        event.preventDefault();

        const formData = new FormData();
        formData.append('file', file);
        formData.append('fileType', fileType)
        formData.append('tags', tags)

        try{
            await api.post('/memoria', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            })
            .then((response)=>{
                console.log(response.data)
            })

        } catch (error){
            console.error('Error:', error)
        }

    }

    return (
        <Container>
            <section>
                <h3>Buscador de memórias</h3>
                <Row>
                    <Col md={10}>
                        <article>
                            <Form.Group controlId="formFile" className="mb-3">
                                <Form.Control type="file" onChange={(e) => setFile(e.target.files[0])} disabled={!fileType} accept={fileType} />
                            </Form.Group>
                        </article>  
                    </Col>
                    <Col md={2}>
                        <article>
                            <Form.Select aria-label="Escolha o formato do arquivo" onChange={changeFileType}>
                                <option value="">Escolha o formato</option>
                                <option value=".pdf">PDF</option>
                                <option value="video/mp4">MP4</option>
                            </Form.Select>
                        </article>
                    </Col>
                </Row>
                <Row>
                    <Col md={12} className="mb-3">
                        <article>
                            <InputGroup className="mb-3">
                                <FormControl placeholder="Add a tag" value={inputValue} onChange={(e) => setInputValue(e.target.value)} onKeyDown={handleAddTag} />
                                <Button variant="outline-secondary" onClick={handleAddTag}> <i className="bi bi-plus"></i> </Button>
                            </InputGroup>
                            <div className="tag-container">
                                {tags.map((tag, index) => (
                                    <Badge pill bg="primary" key={index} className="mr-4 badge-custom" onClick={() => handleDeleteTag(tag)}>
                                        {tag} <span aria-hidden="true">&times;</span>
                                    </Badge>
                                ))}
                            </div>
                        </article>
                    </Col>
                </Row>
                <Row>
                    <Col md={12}>
                        <article>
                            <Button variant="primary" type="submit" onClick={handleSubmit}>
                                Processar
                            </Button>
                        </article>
                    </Col>
                </Row>
            </section>
        </Container>
    )
}

export default Buscador;