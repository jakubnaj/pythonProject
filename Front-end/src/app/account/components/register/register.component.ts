import { Component, OnInit } from "@angular/core";
import { AccountService } from "../../services/account.service";
import { HttpErrorResponse } from "@angular/common/http";
import { NgForm } from "@angular/forms";
import { User } from "../../models/user";
import { ApiError } from "../../models/apiError";

@Component({
  selector: "app-register",
  templateUrl: "./register.component.html",
  styleUrls: ["./register.component.scss"]
})
export class RegisterComponent implements OnInit {
  error: String;
  responseMessage: String;
  constructor(private accountService: AccountService) {}

  ngOnInit() {}

  createUser(user: NgForm) {
    let newUser: User;
    if(user.value.password !== user.value.repeatPassword){
      this.error = "Passwords must be the same";
      return;
    }
    this.accountService.registerUser(user.value).subscribe(
      (data: ApiError)=>{
        if(data){
          this.error = "";
          this.responseMessage = data.message; 
        }
    },
      (error: HttpErrorResponse)=>{
      this.responseMessage = "";
      this.error = error.error.message;
    })
    
  } 
}
