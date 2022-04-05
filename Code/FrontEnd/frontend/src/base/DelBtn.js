import React from "react";
import {Text, TouchableOpacity } from 'react-native';
import styles from '../static/style.js';

export default function DelButton({text, onPress}) {
  return (
    <TouchableOpacity onPress={onPress} style ={styles.del-button}>
      <Text style={styles.textInBtn}>{text}</Text>
    </TouchableOpacity>
  )
}