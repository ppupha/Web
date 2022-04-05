import { StyleSheet } from 'react-native';
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#C3D3D4',
    alignItems: 'center',
    justifyContent: 'flex-start',
  },
  del-button:{
    background: #DF3712;
    border: 1px solid #E3DADA;
    box-sizing: border-box;
    border-radius: 10px;
  },
  infor-button:{
    alignSelf:'center',
    borderRadius: 10,
    background: '#DF3712',
    border: 1px solid #E3DADA;
    box-sizing: border-box;
    border-radius: 10px;
  },
  edit-button:{
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    padding: 0px;
    position: relative;
    width: 66px;
    height: 26px;
  }
  textInBtn:{
    fontSize : 20,
    fontWeight:'bold',
    color:'#000000',
    marginTop:10,
    textAlign:'center'},
  textInfo:{
    fontSize : 18,
    color:'#000000',
    marginTop:5,
    marginLeft:10,
  },
  board:{
    width:410,
    height: 220,
    borderRadius: 15,
    backgroundColor: '#EDE3E3',
    borderColor:'#000000',
    borderWidth:2,
  }

});

export default styles;