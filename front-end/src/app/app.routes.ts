import { Routes } from '@angular/router';
import { Home } from './pages/home/home';
import { Auth } from './pages/auth/auth';
import { Cadastro } from './pages/cadastro/cadastro';
import { Importdados } from './pages/importdados/importdados';
import { Vendedores } from './pages/vendedores/vendedores';

export const routes: Routes = [
    {
        path: '', component: Home,
    },
    {
        path: 'auth', component: Auth
    },
    {
        path: 'cadastro', component: Cadastro
    },
    {
        path:  'importardados', component: Importdados
    },
    {
        path: 'vendedores', component: Vendedores
    }
];
