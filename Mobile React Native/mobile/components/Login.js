import { StatusBar } from 'expo-status-bar';
import React, { useState, useEffect } from 'react';
import { StyleSheet, Text, TextInput, View, Image, Alert, SafeAreaView } from 'react-native';
import { Button, ActivityIndicator } from 'react-native-paper';

const Login = ({ navigation }) => {
    const [loading, setLoading] = useState(false);
    const [rut, setRut] = useState('');
    const [password, setPassword] = useState('');
    const [data, setData] = useState([]);

    const getUsers = async () => {
        try {
          const response = await fetch('http://localhost:3001/api/users');
          const users = await response.json();
          setData(users);
          console.log(users)
        } catch (error) {
          console.error(error);
        } finally {
        }
      };
    
      useEffect(() => {
        getUsers();
      }, []);

    const handleButtonPress = () => {
        navigation.navigate('Home');
    };

    return (
        <SafeAreaView style={styles.container}>
            <View style={styles.header}>
                <View style={styles.green}></View>
                <View style={styles.blue}></View>
                <View style={styles.gray}></View>
            </View>
            <View style={styles.body}>
                <Text style={styles.title}>Colegio del Norte</Text>
                <Text style={styles.subtitle1}>¡Hola!</Text>
                <Text style={styles.subtitle2}>Iniciar sesión</Text>
                {loading && <ActivityIndicator style={styles.activityIndicator} color='#00A898' />}
                <View style={styles.form}>
                    <Text style={styles.label}>Rut</Text>
                    <TextInput
                        style={styles.input}
                        placeholder='123456789'
                        placeholderTextColor='#ccc'
                        value={rut}
                    />
                    <Text style={styles.label}>Contraseña</Text>
                    <TextInput
                        style={styles.input}
                        placeholder='********'
                        placeholderTextColor='#ccc'
                        value={password}
                    />
                </View>

                <StatusBar style="auto" />
                <Button
                    style={styles.button}
                    mode="contained"
                    onPress={() => handleButtonPress()}
                    contentStyle={styles.buttonContent}
                    labelStyle={styles.buttonLabel}
                >
                    Iniciar
                </Button>
            </View>
            <View style={styles.footer}>
                <View style={styles.gray}></View>
                <View style={styles.blue}></View>
                <View style={styles.green}></View>
            </View>
        </SafeAreaView>

    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        alignItems: 'center',
        justifyContent: 'center',
    },
    header: {
        alignSelf: 'stretch',
        justifyContent: 'space-between',
        alignItems: 'flex-start',
    },
    body: {
        width: '100%',
        flex: 1,
        alignItems: 'center',
        justifyContent: 'center',
    },
    footer: {
        alignSelf: 'stretch',
        justifyContent: 'space-between',
        alignItems: 'flex-end',
    },
    green: {
        backgroundColor: '#4DC639',
        width: '100%',
        height: 20,
    },
    blue: {
        backgroundColor: '#146FA1',
        width: '87%',
        height: 20,
    },
    gray: {
        backgroundColor: '#D2D2D2',
        width: '74%',
        height: 20,
    },
    title: {
        fontSize: 36,
        color: '#146FA1',
        fontFamily: 'Inika',
        paddingBottom: 5
    },
    subtitle1: {
        fontSize: 20,
        color: 'black',
        fontFamily: 'Inika',
        paddingBottom: 5
    },
    subtitle2: {
        fontSize: 16,
        color: '#929292',
        fontFamily: 'Inika',
        paddingBottom: 10
    },
    form: {
        width: '80%',
    },
    label: {
        fontSize: 16,
        color: 'black',
        textAlign: 'left',
        fontFamily: 'Inika',
        marginBottom: 5,
        marginLeft: 10,
    },
    input: {
        paddingLeft: 15,
        height: 40,
        borderRadius: 20,
        marginBottom: 20,
        backgroundColor: '#fff',
        shadowColor: '#000',
        shadowOffset: {
            width: 0,
            height: 2,
        },
        shadowOpacity: 0.25,
        shadowRadius: 3.84,
        elevation: 5,
    },
    button: {
        height: 40,
        marginTop: 10,
        width: 150,
        backgroundColor: '#146FA1',
        shadowColor: '#000',
        shadowOffset: {
            width: 0,
            height: 2,
        },
        shadowOpacity: 0.25,
        shadowRadius: 3.84,
        elevation: 5,
    },
    buttonLabel: {
        fontFamily: 'Inika',
    },
    activityIndicator: {
        marginTop: 20
    }
});

export default Login;