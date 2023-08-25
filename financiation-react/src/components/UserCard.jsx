import React, {useContext, useEffect, useState} from 'react';
import {Col, Container, Row} from 'react-bootstrap';
import "../assets/styles/AdvisorCard.css";
import AuthContext from "../context/AuthContext";
import Avatar from '@mui/material/Avatar';
import Card from '@mui/material/Card';
import Checkbox from '@mui/material/Checkbox';
import {Zoom} from "@mui/material";
import {getUserStatusesById} from "../services/StatusServices";
import {getUserRolesById} from "../services/RoleServices";


export const UserCard = ({user}) => {

    const label = { inputProps: { 'aria-label': 'Checkbox demo' } };
    let {authTokens} = useContext(AuthContext)
    let [role, setRole] = useState([])
    let [status, setStatus] = useState([])

    useEffect(() => {
        getUserStatusesById(authTokens.access, user.id_user_status).then(data => setStatus(data))
        getUserRolesById(authTokens.access, user.id_role).then(data => setRole(data))
    }, [])

    return (
        <>
                <Zoom in style={{ transitionDelay: '200ms'}}>
                <div className={'UserCard font'}>
                    <Container>
                    <Card className='UserCard font'>
                        <Container className='UserCard'>
                            <Row key={user.id}>
                                <Col md={1} xs={1} className='profileimage'>
                                    <Avatar className='avatar' alt="Remy Sharp" src={user?.profile_picture}/>
                                </Col>
                                <Col xs={3} md={3} className='name'>
                                    <Row>
                                        <Col>
                                            <strong>
                                                <a>{user.first_name} {user.last_name}</a>
                                            </strong>
                                        </Col>
                                    </Row>
                                    <Row>
                                        <small>{role.name}</small>
                                    </Row>
                                </Col>
                                {status.name === 'Disponible' ? (
                                        <Col xs={3} md={3} className='status'>
                                            <a>{status.name} <a className='circle_green'></a></a>
                                        </Col>
                                    ):(
                                        <Col xs={3} md={3} className='status'>
                                            <a>{status.name} <a className='circle_red'></a></a>
                                        </Col>
                                    )
                                }
                                {status.name === 'Disponible' ? (
                                    <Col xs={2} md={3} className='role content-select'>
                                        <select placeholder="Rol en grupo" className='form-select ' name="Role">
                                            <option value="none" selected disabled hidden>Seleccionar</option>
                                            <option>Coordinador</option>
                                            <option>Asesor</option>
                                        </select>
                                        <i></i>
                                    </Col>
                                    ) : (
                                    <Col xs={5} md={5} className='roleocupado'>
                                        <a>Este usuario se encuentra ocupado</a>
                                    </Col>
                                    )
                                }
                                {status.name === 'Disponible' ? (
                                        <Col xs={2} md={2} className='check'>
                                            <Row>
                                                <input type="checkbox" className='check' />
                                            </Row>
                                        </Col> 
                                    ) : (
                                        <Col>
                                        </Col>
                                    )
                                }
                                 
                            </Row>
                        </Container>
                    </Card>
                    </Container>
                </div>
                </Zoom>
        </>
    )
}

export default UserCard;