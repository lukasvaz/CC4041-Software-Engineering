    
    async function updateTable(e) {
        const selectType = document.getElementById('transaction_type');
        var selectedType = selectType.value;
        const response = await fetch(`get-table/${selectedType}`)
        const data = await response.json();
        console.log(data)
        var tableBody=document.getElementById('home-table-body')
        tableBody.innerHTML='';

        for(var i in data){
            var transaction=data[i];
            tableBody.innerHTML+=`<tr>\
            <th>${transaction['set_at']}</th>\
            <td>${transaction['description']}</td>\
            <td>${transaction['amount']}</td>\
            <td>${transaction['category']}</td>\
            <td>${transaction['type']}</td>
            <td><i class="fa-solid fa-pen"></i> <i class="fa-sharp fa-solid fa-trash"></i></td></tr>`
            /*ultima  columna  es para  para borrar y modificar, si quieren acceder al id  de la transaccion  deben pedir transaction['id'], 
            como  está  todo en una tabla  se debe recuperar si  es  Ingreso o Egreso */
            console.log(transaction['id'])
                        }    
            
        var table=$('#home-table').DataTable({
            paging:true,
            searching:false,
            ordering:false,
            info:false,
            searching:false,
            autowidth:true,
            lengthChange:false,
        });
        table.column('0').order('desc').draw()
    }
    