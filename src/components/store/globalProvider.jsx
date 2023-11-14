import { useState } from 'react'
import DataContext from './dataContext'

function GlobalProvider(props){
    const [cart,setCart] = useState([]);
    const [user, setUser]= useState({name: 'Jesenia'});

    function addToCart(product){
       let copy = [...cart];

           let found = false
            for (let i=0; i<cart.length; i++){
              const item = cart[i];
              if (item._id == product._id){
                found = true;
                item.quantity += product.quantity;
              }
             
          }
          if (!found){
            copy.push(product);
          }
     
      

        setCart(copy);
    }

    function removeFromCart(){}
    return(
        <DataContext.Provider 
        value={{
            cart: cart,
            user: user,
            addToCart: addToCart,
            removeFromCart: removeFromCart,

        }}
        >
        {props.children}
        </DataContext.Provider>
    
    );
}
export default GlobalProvider;