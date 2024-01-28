import { View, Text} from 'react-native'
import React from 'react'
import Login from '../components/Login';
import Home from '../components/Home';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

const Stack = createNativeStackNavigator();

export const Navigator = () => {
    return(
        <Stack.Navigator>
        <Stack.Screen name="Home" component={Home}  options={{ headerShown: false }}/>
        <Stack.Screen name="Login" component={Login} options={{ headerShown: false }} />
        
      </Stack.Navigator>
    )
}