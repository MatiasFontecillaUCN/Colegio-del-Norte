import { StatusBar } from 'expo-status-bar';
import React, { useState, useEffect } from 'react';
import { StyleSheet, Text, TextInput, View, Image, Alert, SafeAreaView } from 'react-native';
import { Button, ActivityIndicator } from 'react-native-paper';

const Home = () => {
    return (
        <SafeAreaView style={styles.container}>
            <View style={styles.header}>
                <View style={styles.green}></View>
                <View style={styles.blue}></View>
                <View style={styles.gray}></View>
            </View>
            <View style={styles.body}>
                <Text style={styles.title}>¡Hola!</Text>
                <Text style={styles.subtitle1}>Ricardo Urvina</Text>
                <Text style={styles.subtitle2}>¿Qué deseas hacer?</Text>
                <StatusBar style="auto" />
                <Button
                    style={styles.button}
                    mode="contained"
                    onPress={() => handleButtonPress()}
                    contentStyle={styles.buttonContent}
                    labelStyle={styles.buttonLabel}
                >
                    Mis matrículas
                </Button>
                <Button
                    style={styles.button}
                    mode="contained"
                    onPress={() => handleButtonPress()}
                    contentStyle={styles.buttonContent}
                    labelStyle={styles.buttonLabel}
                >
                    Mis alumnos
                </Button>
                <Button
                    style={styles.button}
                    mode="contained"
                    onPress={() => handleButtonPress()}
                    contentStyle={styles.buttonContent}
                    labelStyle={styles.buttonLabel}
                >
                    Ver profesores
                </Button>
                <View style={styles.bodyEnd}>
                    <Button
                        style={styles.buttonExit}
                        mode="contained"
                        onPress={() => handleButtonPress()}
                        contentStyle={styles.buttonContent}
                        labelStyle={styles.buttonLabel}
                    >
                        Salir
                    </Button>
                </View>
            </View>
            <View style={styles.footer}>
                <View style={styles.gray}></View>
                <View style={styles.blue}></View>
                <View style={styles.green}></View>
            </View>
        </SafeAreaView>
    )
};


const styles = StyleSheet.create({
    container: {
        flex: 1,
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
        color: 'black',
        fontFamily: 'Inika',
        marginTop: '10%',
        paddingBottom: 5
    },
    subtitle1: {
        fontSize: 20,
        color: '#929292',
        fontFamily: 'Inika',
        paddingBottom: 5
    },
    subtitle2: {
        fontSize: 20,
        color: '#146FA1',
        fontFamily: 'Inika',
        marginTop: '15%',
        paddingBottom: '10%'
    },
    button: {
        height: 40,
        width: 200,
        marginBottom: '5%',
        backgroundColor: '#4DC639',
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
    bodyEnd: {
        marginTop: '40%',
        justifyContent: 'center',
    },
    buttonExit: {
        height: 40,
        width: 200,
        marginTop: '20%',
        backgroundColor: '#D12B35',
        shadowColor: '#000',
        shadowOffset: {
            width: 0,
            height: 2,
        },
        shadowOpacity: 0.25,
        shadowRadius: 3.84,
        elevation: 5,
    },
});
export default Home