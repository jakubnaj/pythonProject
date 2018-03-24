import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule }   from '@angular/forms';
import {RouterModule} from '@angular/router';

import { LoginComponent } from './components/login/login.component';
import { RegisterComponent } from './components/register/register.component';
import { ForgotPasswordComponent } from './components/forgot-password/forgot-password.component';
import { ResetPasswordComponent } from './components/reset-password/reset-password.component';
import { AccountService } from './services/account.service';


@NgModule({
  imports: [
    CommonModule,
    RouterModule,
    FormsModule
  ],
  declarations: [LoginComponent, RegisterComponent, ForgotPasswordComponent, ResetPasswordComponent],
  providers: [AccountService],
  exports: [LoginComponent,RegisterComponent, ForgotPasswordComponent, ResetPasswordComponent]
})
export class AccountModule { }
