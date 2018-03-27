import { Component, OnInit } from "@angular/core";
import { Router } from "@angular/router";
import { AuthService } from "../../../shared/services/auth.service";
import { NgForm } from "@angular/forms";

@Component({
  selector: "app-login",
  templateUrl: "./login.component.html",
  styleUrls: ["./login.component.scss"]
})
export class LoginComponent implements OnInit {
  error: String;
  constructor(private authService: AuthService, private router: Router) {}

  ngOnInit() {}
  login(form: NgForm) {
    this.authService.login(form.value.username, form.value.password).subscribe(
      data => {
        this.error = "";
        this.router.navigate([""]);
      },
      error => {
        console.log(error.status);
        if (error.status === 401) {
          console.log("pipsa");
          this.error = "Wrong Credentials";
        } else {
          this.error = error.message;
        }
      }
    );
  }
}
