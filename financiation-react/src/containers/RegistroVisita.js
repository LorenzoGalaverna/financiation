import React, { useState } from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import "../assets/styles/registrovisita.css"
import "primereact/resources/primereact.min.css";
import Container from "react-bootstrap/esm/Container";
import Button from 'react-bootstrap/Button';
import { Form, Row } from 'react-bootstrap';

export default function RegistroVisita() {

    const localidades = [
        'Ciudad A',
        'Ciudad B',
        'Ciudad C',
        'Ciudad D',
        'Ciudad E',
    ];

    const lugar = [
        'Ciudad A',
        'Ciudad B',
        'Ciudad C',
        'Ciudad D',
        'Ciudad E',
    ];

    const grupo = [
        'Grupo 1',
        'Grupo 2',
        'Grupo 3',
        'Grupo 4',
        'Grupo 5',
    ];

    const visitstatus = [
        'Confirmado',
        'Pendiente',
    ];

    const agreement = [
        'Si',
        'No',
    ];

    const contactedreferrer = [
        'Ventas',
        'Marketing',
        'Desarrollo',
        'Recursos Humanos',
        'Operaciones',
    ];

    const address = [
        'Si',
        'No',
    ];

    const logo = [
        'Si',
        'No',
    ];

    return (
        <Container fluid id="RegistroVisita">

            <Container id="Rowcontent">
                <Container>
                    <Row>
                        <h2 id="tittle">Registro de Visitas</h2>
                    </Row>
                </Container>
                <Container>
                    <Row>
                        <Form.Control id="input" type="text" placeholder="Flyer" />
                        <Form.Control id="input" type="text" placeholder="Distancia" />
                        <Form.Control id="input" type="time" placeholder="Tiempo de Viaje" />
                    </Row>
                </Container>
                <Container>
                    <Row >
                        <Form.Control type="date" id="input" name="dob" placeholder="Fecha Visita" />
                        <Form id="input">
                            <Form.Check  >
                                <Form.Check.Input />
                                <Form.Check.Label>Registro Civil</Form.Check.Label>
                            </Form.Check>
                        </Form>
                        <Form.Control id="input" type="text" placeholder="Hospedaje" />
                    </Row>
                </Container>
                <Container>
                    <Row >
                        <Form id="input">
                            <Form.Check  >
                                <Form.Check.Input />
                                <Form.Check.Label>Modernization Fund</Form.Check.Label>
                            </Form.Check>
                        </Form>
                        <Form.Control id="input" type="time" placeholder="Start Time" />
                        <Form.Control id="input" type="time" placeholder="Finish Time" />
                    </Row>
                </Container>
                <Container>
                    <Row >
                        <Form.Control id="input" as="select"><option value="">Lugar</option>{lugar.map((lugar, index) =>
                            (<option key={index} value={lugar}>{lugar}</option>))}</Form.Control>
                        <Form.Control id="input" as="select"><option value="">Localidad</option>{localidades.map((localidad, index) =>
                            (<option key={index} value={localidad}>{localidad}</option>))}</Form.Control>
                        <Form.Control id="input" as="select"><option value="">Grupo</option>{grupo.map((grupo, index) =>
                            (<option key={index} value={grupo}>{grupo}</option>))}</Form.Control>
                    </Row>
                </Container>
                <Container>
                    <Row>
                        <Form.Control id="input" as="select"><option value="">Visit Status</option>{visitstatus.map((visitstatus, index) =>
                            (<option key={index} value={visitstatus}>{visitstatus}</option>))}</Form.Control>
                        <Form.Control id="input" as="select"><option value="">Agreement</option>{agreement.map((agreement, index) =>
                            (<option key={index} value={agreement}>{agreement}</option>))}</Form.Control>
                        <Form.Control id="input" as="select"><option value="">Contacto Referente</option>{contactedreferrer.map((contactedreferrer, index) =>
                            (<option key={index} value={contactedreferrer}>{contactedreferrer}</option>))}</Form.Control>
                    </Row>
                </Container>
                <Container>
                    <Row>
                        <Form.Control id="input" as="select"><option value="">Address</option>{address.map((address, index) =>
                            (<option key={index} value={address}>{address}</option>))}</Form.Control>
                        <Form.Control id="input" as="select"><option value="">Logo</option>{logo.map((logo, index) =>
                            (<option key={index} value={logo}>{logo}</option>))}</Form.Control>
                    </Row>
                </Container>
                <Container>
                    <Row className="justify-content-center align-items-center">
                        <Button id="bt1" variant="primary">Registar</Button>{' '}
                    </Row>
                </Container>
            </Container>

        </Container>

    )
}






